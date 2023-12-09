// 这个示例程序展示goroutine调度器是如何在单个线程上切分时间片的
package main

import (
	"fmt"
	"runtime"
	"sync"
)

// wg用来等待程序完成
var wg sync.WaitGroup

func main() {
	// 分配一个逻辑处理器给调度器使用
	// runtime.GOMAXPROCS(1)

	// 分配两个逻辑处理器给调度器使用，
	// 乱序输出，B会先调度，所以先结束。
	runtime.GOMAXPROCS(2)

	// 计数加2，表示要等待两个goroutine
	wg.Add(2)

	// 创建两个goroutine
	fmt.Println("Create Goroutines")
	go printPrime("A")
	go printPrime("B")

	// 等待goroutine结束
	fmt.Println("Waiting To Finish")
	wg.Wait()

	fmt.Println("Terminateing Program")
}

// 寻找5000以内的素数的函数
func printPrime(prefix string) {
	defer wg.Done()
next:
	for outer := 2; outer < 5000; outer++ {
		for inner := 2; inner < outer; inner++ {
			if outer%inner == 0 {
				continue next
			}
		}
		fmt.Printf("%s:%d\n", prefix, outer)
	}
	fmt.Println("Completed", prefix)
}
