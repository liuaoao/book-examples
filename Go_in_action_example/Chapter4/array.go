package main

import (
	"fmt"
)

func main() {
	// *访问指针
	// 声明包含5个元素的指向整数的的数组
	// 用整型指针初始化索引为0和1的数组元素
	array := [5]*int{0: new(int), 1: new(int)}

	// 为索引为0和1的元素赋值
	*array[0] = 10
	*array[1] = 20
	fmt.Println(array)

	// 多维数组
	// var array [4][2]int
	array1 := [4][2]int{{10, 11}, {20, 21}, {30, 31}, {40, 41}}
	fmt.Println(array1[0][0])

	// 复制array1
	var array2 [4][2]int
	array2 = array1
	// array2 := array1 // 也可以这样，声明并初始化
	// var array2 [4][2]int = array1 // 也可以这样，声明并初始化
	fmt.Println(array2[0][1])

	// 将array1的索引1的维度复制到一个同类型的新数组里
	var array3 [2]int = array1[1]
	fmt.Println(array3)
	var v int = array1[1][1]
	fmt.Println(v)
}
