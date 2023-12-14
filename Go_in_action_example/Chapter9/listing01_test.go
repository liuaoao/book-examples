// 这个示例程序展示如何写基础单元测试
package listing01

import (
	"net/http"
	"testing"
)

// 打勾和打×的符号
const checkMark = "\u2713"
const ballotX = "\u2717"

// TestDownload确认http包的Get函数可以下载内容
func TestDownload(t *testing.T) {
	url := "http://www.goinggo.net/index.xml"
	statusCode := 200

	t.Log("Given the need to test downloading content.")
	{
		// \t是tab换行符
		// 使用t.Log来输出测试消息，Logf是格式化消息的版本
		// 需要执行go test -v中的-v才能看到输出
		t.Logf("\tWhen checking \"%s\" for status code \"%d\"",
			url, statusCode)
		{
			resp, err := http.Get(url)
			if err != nil {
				// t.Fatal方法让测试框架知道这个测试失败了。
				// 还可以另外输出一些消息。
				// 对应的格式化消息版本是t.Fatalf
				t.Fatal("\t\tShould be able to make the Get call.",
					ballotX, err)
			}
			t.Log("\t\tShould be able to make the Get call.",
				checkMark)

			defer resp.Body.Close()

			if resp.StatusCode == statusCode {
				t.Logf("\t\tShould receive a \"%d\" status. %v",
					statusCode, checkMark)
			} else {
				// t.Errorf方法不会停止当前测试函数的执行。
				t.Errorf("\t\tShould receive a \"%d\" status. %v %v",
					statusCode, ballotX, resp.StatusCode)
			}
		}
	}
}
