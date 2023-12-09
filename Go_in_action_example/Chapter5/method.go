package main

import (
	"fmt"
)

// user在程序里定义一个用户类型
type user struct {
	name  string
	email string
}

// notify使用值接收者实现了一个方法
func (u user) notify() {
	fmt.Printf("Sending User Email to %s<%s>\n",
		u.name, u.email)
}

// changeEmail使用指针接收者实现了一个方法
func (u *user) changeEmail(email string) {
	u.email = email
}

// main是程序的入口
func main() {
	// user类型的值可以用来调用
	// 使用值接收者声明的方法
	bill := user{"Bill", "bill@email.com"}
	bill.notify()

	// 指向user类型值的指针也可以用来调用
	// 使用值接收者声明的方法
	// （Go编译器会自动处理）
	lisa := &user{"Lisa", "lisa@email.com"}
	lisa.notify()

	// user类型的值可以用来调用
	// 使用指针接收者声明的方法
	bill.changeEmail("bill@newdomain.com")
	bill.notify()

	// 指向user类型值的指针可以用来调用
	// 使用指针接收者声明的方法
	// （Go编译器会自动处理）
	lisa.changeEmail("lisa@comcase.com")
	lisa.notify()
}
