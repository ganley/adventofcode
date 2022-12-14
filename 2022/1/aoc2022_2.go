package main

import (
    "bufio"
    "fmt"
    "os"
    "sort"
    "strconv"
)

func main() {
    var a []int
    var s int = 0

    scanner := bufio.NewScanner(os.Stdin)
    for scanner.Scan() {
	    if len(scanner.Text()) == 0 {
            a = append(a, s)
            s = 0
        } else {
            i, _ := strconv.Atoi(scanner.Text())
            s += i
        }
    }

    sort.Ints(a)

    fmt.Println(a[len(a) - 1] + a[len(a) - 2] + a[len(a) - 3])
}

