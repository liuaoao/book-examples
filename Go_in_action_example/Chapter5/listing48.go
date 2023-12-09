// 这个示例程序使用接口展示多态行为
package main

import (
	"fmt"
)

// notifer是一个定义了通知类的接口
type notifier interface {
	notify()
}

// user在程序里定义一个用户类型
type user struct {
	name  string
	email string
}

// notify是使用指针接收者实现的了notifier接口
func (u *user) notify() {
	fmt.Println("Sending user email to %s<%s>\n",
		u.name,
		u.email)
}

// admin定义了程序里的管理员
type admin struct {
	name  string
	email string
}

// notify是使用指针接收者实现的了notifier接口
func (a *admin) notify() {
	fmt.Println("Sending admin email to %s<%s>\n",
		a.name,
		a.email)
}

// main是程序的入口
func main() {
	// 创建一个user类型的值，并发送通知
	bill := user{"Bill", "bill@email.com"}
	sendNotification(&bill)

	// 创建一个admin类型的值，并发送通知
	lisa := admin{"Lisa", "lisa@email.com"}
	sendNotification(&lisa)

}

func sendNotification(n notifier) {
	n.notify()
}
