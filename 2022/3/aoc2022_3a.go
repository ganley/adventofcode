package main

import (
    "bufio"
    "fmt"
    "os"
)


func priority(c byte) int {
    if c >= 'a' && c <= 'z' {
        return int(c) - int('a') + 1
    }
    return int(c) - int('A') + 27
}


func main() {
    var s int = 0

    scanner := bufio.NewScanner(os.Stdin)
    for scanner.Scan() {
        var t = scanner.Text()
        var h = len(t) / 2
        var f[128] bool
        for i := 0; i < h; i++ {
            f[int(t[i])] = true
        }
        for i := h; i < len(t); i++ {
            if f[int(t[i])] {
                f[int(t[i])] = false
                s += priority(t[i])
            }
        }
    }

    fmt.Println(s)
}

