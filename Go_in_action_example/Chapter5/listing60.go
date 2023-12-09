// 这个示例程序展示如何将将嵌入类型应用于接口
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

// notify实现了一个可以通过user类型值的指针调用的方法
func (u *user) notify() {
	fmt.Printf("Sending user email to %s<%s>\n",
		u.name,
		u.email)
}

// admin代表一个拥有权限的管理员用户
type admin struct {
	user  // 嵌入类型
	level string
}

// 通过admin类型值的指针调用的方法
func (a *admin) notify() {
	fmt.Printf("Sending admin email to %s<%s>\n",
		a.name,
		a.email)
}

// main是应用程序的入口
func main() {
	// 创建一个admin用户
	ad := admin{
		user: user{
			name:  "jogn smith",
			email: "john@yahoo.com",
		},
		level: "super",
	}

	// 给admin用户发送一个通知
	// 接口的嵌入的内部类型实现并没有提升到外部类型
	sendNotification(&ad)

	// 我们可以直接访问内部类型的方法
	ad.user.notify()

	// 内部类型的方法没有被提升到外部类型
	ad.notify()
}

// sendNotification接受一个实现了notifier接口的值
// 并发送通知
func sendNotification(n notifier) {
	n.notify()
}
