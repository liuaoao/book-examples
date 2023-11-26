package search

import (
	"log"
	"sync"
)

// A map of registered matchers for searching.
// 注册用于搜索的匹配器映射
// key是string类型，value是Matcher类型
var matchers = make(map[string]Matcher)

// Run performs the search logic.
// Run执行搜索逻辑
func Run(searchTerm string) {
	// Retrieve the list of feeds to search through.
	// 获取需要搜索的数据源列表
	// 返回两个值，第一个是Feed类型的切片
	feeds, err := RetrieveFeeds()
	if err != nil {
		// Fatal函数接受这个错误的值，并将错误在终端窗口里输出，随后终止程序
		log.Fatal(err)
	}

	// Create an unbuffered channel to receive match results to display.
	// 创建一个无缓冲的通道，接受匹配后的结果
	results := make(chan *Result)

	// Setup a wait group so we can process all the feeds.
	// 构造一个waitGroup，以便处理所有的数据源
	var waitGroup sync.WaitGroup

	// Set the number of goroutines we need to wait for while
	// they process the individual feeds.
	// 设置需要等待处理
	// 每个数据源的goroutine的数量
	waitGroup.Add(len(feeds))

	// Launch a goroutine for each feed to find the results.
	// 为每个数据源启动一个goroutine来查找结果
	for _, feed := range feeds {
		// Retrieve a matcher for the search.
		// 获取一个匹配器用以查找
		// 如果指定了第二个值，就会返回一个布尔标志，
		// 来表示查找的键是否存在与map里
		matcher, exists := matchers[feed.Type]
		if !exists {
			// 如果这个feed type不存在在matchers的map里
			// 则使用默认的匹配器
			// 这样程序就算不知道数据源的具体类型，也可以执行而不会中断
			matcher = matchers["default"]
		}

		// Launch the goroutine to perform the search.
		// 启动一个goroutine来执行搜索
		// 关键字go来启动了一个匿名函数作为goroutine，
		go func(matcher Matcher, feed *Feed) {
			// 这个匿名函数接受了两个参数
			// 一个类型为Matcher
			// 一个是指向了Feed类型值的指针
			// Match函数会搜索数据源的数据，并将匹配结果输出到results通道
			Match(matcher, feed, searchTerm, results)
			// 一旦搜索完毕，递减WaitGroup的计数
			// 这里使用了闭包，
			// 函数可以直接访问到没有作为参数传入的变量waitGroup
			// 所有的goroutine因为闭包共享同样的变量
			waitGroup.Done()
		}(matcher, feed)
	}

	// Launch a goroutine to monitor when all the work is done.
	// 启动一个goroutine来监控是否所有的工作都做完了
	go func() {
		// Wait for everything to be processed.
		// 等候所有任务完成
		// 当waitGroup内部的计数达到0
		waitGroup.Wait()

		// Close the channel to signal to the Display
		// function that we can exit the program.
		// 用关闭通道的方式，通知display函数
		// 可以退出程序了
		close(results)
	}()

	// Start displaying results as they are available and
	// return after the final result is displayed.
	// 启动函数，显示返回的结果，并且
	// 在最后一个结果显示完后返回
	Display(results)
}

// Register is called to register a matcher for use by the program.
// Register调用时，会注册一个匹配器，提供给后面的程序使用
// 这个函数的职责时，将一个Matcher值加入到保存注册匹配器的映射中(matchers)
// 所有都应该在main函数被调用前完成，使用init函数就可以做到这种初始化了
func Register(feedType string, matcher Matcher) {
	if _, exists := matchers[feedType]; exists {
		log.Fatalln(feedType, "Matcher already registered")
	}

	log.Println("Register", feedType, "matcher")
	matchers[feedType] = matcher
}