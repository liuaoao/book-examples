// 这个示例程序展示如何写一个基本的表组测试
package listing08

import (
	"net/http"
	"testing"
)

// 打勾和打×的符号
const checkMark = "\u2713"
const ballotX = "\u2717"

// TestDownload确认http包的Get函数可以下载内容
// 并正确处理不同的状态
func TestDownload(t *testing.T) {
	var urls = []struct {
		url        string
		statusCode int
	}{
		// 初始化测试数据
		{
			"http://www.goinggo.net/index.xml",
			http.StatusOK,
		},
		{
			"http://rss.cnn.com/rss/cnn_topstbadurl.rss",
			http.StatusNotFound,
		},
	}

	t.Log("Given the need to test downloading different content.")
	{
		for _, u := range urls {
			t.Logf("\tWhen checking \"%s\" for status code \"%d\"",
				u.url, u.statusCode)
			{
				resp, err := http.Get(u.url)
				if err != nil {
					t.Fatal("\t\tShould be able to make the Get call.",
						ballotX, err)
				}
				t.Log("\t\tShould be able to make the Get call.",
					checkMark)

				defer resp.Body.Close()

				if resp.StatusCode == u.statusCode {
					t.Logf("\t\tShould receive a \"%d\" status. %v",
						u.statusCode, checkMark)
				} else {
					// t.Errorf方法不会停止当前测试函数的执行。
					t.Errorf("\t\tShould receive a \"%d\" status. %v %v",
						u.statusCode, ballotX, resp.StatusCode)
				}
			}
		}
	}
}
