package main

import (
	"fmt"
)

func main() {
	// 创建一个字符串切片
	// 其长度和容量都是5
	slice := make([]string, 5)
	fmt.Println(slice)

	// 创建一个整型切片
	// 其长度为3个元素，容量为5个元素
	slice2 := make([]int, 3, 5)
	fmt.Println(slice2)

	// 创建字符串切片，长度和容量都是5
	slice3 := []string{"red", "blue", "green", "yellow", "pink"}
	fmt.Println(slice3)

	// 创建整型切片，长度和容量都是3
	slice4 := []int{10, 20, 30}
	fmt.Println(slice4)

	// 创建字符串切片，使用空字符串初始化第100个元素
	slice5 := []string{99: ""}
	fmt.Println(slice5)

	// 声明数组和切片的不同
	// 创建一个3个元素的整型数组
	array := [3]int{1, 2, 3}
	fmt.Println(array)
	// 创建长度和容量都是3的整形切片
	slice6 := []int{1, 2, 3}
	fmt.Println(slice6)

	// 声明一个nil切片
	var slice7 []int
	fmt.Println(slice7)
	//声明一个空切片
	slice8 := []int{}
	slice9 := make([]int, 0)
	fmt.Println(slice8, slice9)

	// 创建一个切片
	slice10 := []int{10, 20, 30, 40, 50}
	// 创建一个新切片
	newslice := slice10[1:3]
	// 修改索引为1的元素
	newslice[1] = 25
	fmt.Println(slice10, newslice)
	// 使用原来的容量来分配一个新元素
	newslice = append(newslice, 60)
	fmt.Println("case 10: ", slice10, newslice)

	// 创建一个切片
	slice11 := []int{10, 20, 30, 40}
	// append后，newslice2会拥有一个全新的底层数组
	// 且容量是原来的两倍
	newslice2 := append(slice11, 50)
	fmt.Println(slice11, newslice2)
	fmt.Println("case 11: ", cap(slice11), cap(newslice2))

	// 创建一个切片
	slice12 := []string{"apple", "orange", "plum", "banana", "grape"}
	// 对第三个元素做切片，并限制容量，长度和容量都是1
	newslice3 := slice12[2:3:3]
	newslice3 = append(newslice3, "kiwi")
	fmt.Println("case 12: ", slice12, newslice3)

	// 迭代每一个元素，并显示其值
	fmt.Println("case 13: ")
	for index, value := range slice12 {
		fmt.Printf("Index %d Values: %s\n", index, value)
	}
	// range返回的第二个值是副本，不是引用
	fmt.Println("case 13: ")
	for index, value := range slice12 {
		fmt.Printf("value %s value-addr: %X elem-addr: %X\n",
			value, &value, &slice12[index])
	}

	// 也可以用传统的for循环
	for index := 2; index < len(slice12); index++ {
		fmt.Printf("Index %d Values: %s\n", index, slice12[index])
	}

}
