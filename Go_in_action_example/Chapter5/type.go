package main

import "fmt"

func main() {
	// user在程序中定义一个用户类型
	// struct是结构类型的意思？
	type user struct {
		name       string
		email      string
		ext        int
		privileged bool
	}

	// 声明user类型的变量
	var bill user
	fmt.Println("case1: ", bill)
	// 声明user类型的变量，并初始化所有字段
	// 对顺序没有要求，但是结尾要有逗号
	lisa := user{
		name:       "Lisa",
		email:      "lisa@email.com",
		ext:        123,
		privileged: true,
	}
	fmt.Println("case2: ", lisa)
	// 习惯上更常用以下的声明方式
	// 对顺序有要求，结尾没有逗号
	lisa2 := user{"Lisa", "lisa@email.com", 123, true}
	fmt.Println("case3: ", lisa2)

	// admin需要一个user类型作为管理者，并附加权限
	type admin struct {
		person user
		level string
	}
	// 声明admin类型的变量
	fred := admin{
		person: user{
			name:       "Lisa",
			email:      "lisa@email.com",
			ext:        123,
			privileged: true,
		},
		level: "super",
	}
	fmt.Println("case4: ", fred)



}
