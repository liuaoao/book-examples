// 这个示例程序展示如何在程序里造成竞争状态
// 实际上不希望出现这种情况
package main

import (
	"fmt"
	"runtime"
	"sync"
	"sync/atomic"
)

var (
	// counter是所有goroutine都要增加其值的变量
	counter int64
	// wg用来等待程序结束
	wg sync.WaitGroup
)

func main() {
	// 计数加2，表示要等待两个goroutine
	// runtime.GOMAXPROCS(2)
	wg.Add(2)

	// 创建两个goroutine
	go incCounter(1)
	go incCounter(2)

	// 等待goroutine结束
	wg.Wait()

	// 输出4
	fmt.Println("Final Counter:", counter)
}

// incCounter增加包里counter变量的值
func incCounter(id int) {
	// 在函数退出时调用Done来通知main函数工作已经完成
	defer wg.Done()

	for count := 0; count < 2; count++ {
		// 安全地对counter加1
		// 方法是强制同一时刻只能由一个goroutine运行并完成这个加法操作
		atomic.AddInt64(&counter, 1)

		// 当前goroutine从线程退出，并放回到队列中
		// 给其他goroutine运行的机会，以便让竞争状态更明显
		runtime.Gosched()
	}
}
