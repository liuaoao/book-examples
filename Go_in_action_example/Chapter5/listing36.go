// 这个示例程序展示Go语言怎么使用接口
package main

import (
	"fmt"
)

// notifer是一个定义了通知类的接口
type notifer interface {
	notify()
}

type user struct {
	name  string
	email string
}

// notify是使用指针接收者实现的方法
func (u *user) notify() {
	fmt.Println("Sending user email to %s<%s>\n",
		u.name,
		u.email)
}

// main是程序的入口
func main() {
	// 创建一个user类型的值，并发送通知
	u := user{"Bill", "bill@email.com"}
	
	// 错误的示例
	// sendNotification(u)
	// 不能将u（类型user）作为sendNotification的参数类型notifier，
	// user类型并没有实现notifier（notify方法使用指针接收者的声明）

	// 正确的用法
	sendNotification(&u)
}

func sendNotification(n notifer) {
	n.notify()
}
