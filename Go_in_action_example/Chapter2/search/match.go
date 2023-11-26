package search

import (
	"log"
)

// Result contains the result of a search.
// Result保存搜索的结果
type Result struct {
	Field   string
	Content string
}

// Matcher defines the behavior required by types that want
// to implement a new search type.
// Matcher定义了要实现的新搜索类型的行为
// 声明了一个名为Matcher的接口类型
// interface关键字声明了一个接口，这个接口声明了结构类型或者具名类型需要实现的行为
// 一个接口的行为最终由在这个接口类型中声明的方法觉得
type Matcher interface {
	// Matcher接口只声明了一个方法Search
	// 这个方法输入一个指向Feed类型值的指针和一个string类型的搜索项
	// 这个方法返回两个值，这个指向Result类型值的指针的切片，一个错误值
	Search(feed *Feed, searchTerm string) ([]*Result, error)
}

// Match is launched as a goroutine for each individual feed to run
// searches concurrently.
// Match函数，为每个数据源单独启动goroutne来执行这个函数
// 并发地执行搜索
func Match(matcher Matcher, feed *Feed, searchTerm string, results chan<- *Result) {
	// Perform the search against the specified matcher.
	// 对特定的匹配器执行搜索
	searchResults, err := matcher.Search(feed, searchTerm)
	if err != nil {
		log.Println(err)
		return
	}

	// Write the results to the channel.
	// 将结果写入通道
	for _, result := range searchResults {
		results <- result
	}
}

// Display writes results to the console window as they
// are received by the individual goroutines.
// Display从每个单独的goroutine接收到结果后从终端中输出
func Display(results chan *Result) {
	// The channel blocks until a result is written to the channel.
	// Once the channel is closed the for loop terminates.
	// 通道会一直被阻塞，直到有结果写入
	// 一旦通道会关闭，for循环会终止
	for result := range results {
		log.Printf("%s:\n%s\n\n", result.Field, result.Content)
	}
}