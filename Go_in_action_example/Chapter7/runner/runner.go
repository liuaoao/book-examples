// Example is provided with help by Gabriel Aszalos.
// Package runner manages the running and lifetime of a process.
package runner

import (
	"errors"
	"os"
	"os/signal"
	"time"
)

// Runner runs a set of tasks within a given timeout and can be
// shut down on an operating system interrupt.
// Runner在给定的超时时间内执行一组任务，并且在操作系统发送
// 中断信号时结束这些任务
type Runner struct {
	// interrupt channel reports a signal from the
	// operating system.
	// interrupt通道报告从操作系统发送的信息
	interrupt chan os.Signal

	// complete channel reports that processing is done.
	// complete通道报告处理任务已经完成
	complete chan error

	// timeout reports that time has run out.
	// timeout通道报错处理任务已经超时
	timeout <-chan time.Time

	// tasks holds a set of functions that are executed
	// synchronously in index order.
	// task持有一组以索引顺序依次执行的函数
	tasks []func(int)
}

// ErrTimeout is returned when a value is received on the timeout channel.
var ErrTimeout = errors.New("received timeout")

// ErrInterrupt is returned when an event from the OS is received.
var ErrInterrupt = errors.New("received interrupt")

// New returns a new ready-to-use Runner.
// New返回一个新的准备使用的Runner
func New(d time.Duration) *Runner {
	return &Runner{
		interrupt: make(chan os.Signal, 1),
		complete:  make(chan error),
		// time.After函数创建了一个定时器，在指定时间后向通道发送一个时间戳
		timeout:   time.After(d),
	}
}

// Add attaches tasks to the Runner. A task is a function that
// takes an int ID.
// Add将一个任务附加到Runner上，这个任务是一个
// 接受一个int类型的ID作为参数的函数
// ...表示可变参数，即可以接受任意数量的该类型的参数
func (r *Runner) Add(tasks ...func(int)) {
	r.tasks = append(r.tasks, tasks...)
}

// Start runs all tasks and monitors channel events.
// Start执行所有任务，并监视通道时间
func (r *Runner) Start() error {
	// We want to receive all interrupt based signals.
	// 我们希望接受所有中断信号
	signal.Notify(r.interrupt, os.Interrupt)

	// Run the different tasks on a different goroutine.
	// 用不同的goroutine执行不同的任务
	go func() {
		r.complete <- r.run()
	}() // 这个括号表示匿名函数被调用

	// select关键字用于处理通道的多路选择
	select {
	// Signaled when processing is done.
	case err := <-r.complete:
		return err

	// Signaled when we run out of time.
	case <-r.timeout:
		return ErrTimeout
	}
}

// run executes each registered task.
// run执行每一个已注册的任务
func (r *Runner) run() error {
	for id, task := range r.tasks {
		// Check for an interrupt signal from the OS.
		// 检测操作系统的中断信号
		if r.gotInterrupt() {
			return ErrInterrupt
		}

		// Execute the registered task.
		task(id)
	}

	return nil
}

// gotInterrupt verifies if the interrupt signal has been issued.
func (r *Runner) gotInterrupt() bool {
	select {
	// Signaled when an interrupt event is sent.
	// 当中断事件被触发时发出的信号
	case <-r.interrupt:
		// Stop receiving any further signals.
		// 停止接受后续的任何信号
		signal.Stop(r.interrupt)
		return true

	// Continue running as normal.
	default:
		return false
	}
}