// 这个程序演示了如何使用通道来见识
// 程序运行的时间，以在程序运行时间过长
// 时如何终止程序
package main

import (
	"log"
	"os"
	"time"

	"./runner"
)

// timeout规定了必须在多少秒内处理完成
const timeout = 15 * time.Second

func main() {
	log.Println("Starting work.")

	// 为本次执行发配超时时间
	r := runner.New(timeout)

	// 加入要执行的任务
	r.Add(createTask(), createTask(), createTask())

	// 执行任务并处理结果
	if err := r.Start(); err != nil {
		switch err {
		case runner.ErrTimeout:
			log.Println("Terminating due to timeout.")
			os.Exit(1)
		case runner.ErrInterrupt:
			log.Println("Terminating due to interrupt.")
			os.Exit(2)
		}
	}
}

// createTask 返回一个根据id
// 休眠指定秒数的示例任务
func createTask() func(int) {
	return func(id int) {
		log.Printf("Processor - Task #%d.", id)
		time.Sleep(time.Duration(id) * time.Second)
	}
}
