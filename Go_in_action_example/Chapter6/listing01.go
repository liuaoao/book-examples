// 这个示例程序展示如何创建goroutine以及调度器的行为
package main

import (
	"fmt"
	"runtime"
	"sync"
)

// main是所有Go程序的入口
func main() {
	// 分配一个逻辑处理器给调度器用
	// runtime.GOMAXPROCS(1)

	// 用两个逻辑处理器的话，那么就会乱序展示
	// runtime.GOMAXPROCS(2)

	// wg用来等待程序外城
	// 计数加2，表示要等待两个goroutine
	var wg sync.WaitGroup
	wg.Add(2)

	fmt.Println("Start Gouroutines")

	// 声明一个匿名函数，并创建一个goroutine
	go func() {
		fmt.Printf("Start lower letter printer")
		// 在函数退出时调用Done来通知main函数工作以及完成
		defer wg.Done()

		// 显示字母表3次
		for count := 0; count < 3; count++ {
			for char := 'a'; char < 'a'+26; char++ {
				fmt.Printf("%c ", char)
			}
		}
	}()

	// 声明一个匿名函数，并创建一个goroutine
	go func() {
		fmt.Printf("Start upper letter printer")
		// 在函数退出时调用Done来通知main函数工作以及完成
		defer wg.Done()

		// 显示字母表3次
		for count := 0; count < 3; count++ {
			for char := 'A'; char < 'A'+26; char++ {
				fmt.Printf("%c ", char)
			}
		}
	}()

	// 等待goroutine结束
	fmt.Println("Waiting To Finish")
	wg.Wait()

	fmt.Println("\nTerminating Program")
}
