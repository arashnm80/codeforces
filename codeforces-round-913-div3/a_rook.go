package main

import (
	// "bufio"
	"fmt"
	// "os"
	"strconv"
)

func main() {
	var t int
	fmt.Scan(&t)

	letters := "abcdefgh"

	for caseNum := 0; caseNum < t; caseNum++ {
		var s string
		fmt.Scan(&s)

		letter := string(s[0])
		number, _ := strconv.Atoi(string(s[1]))

		// Loop for numbers
		for i := 1; i <= 8; i++ {
			if i != number {
				fmt.Println(letter + strconv.Itoa(i))
			}
		}

		// Loop for letters
		for _, ch := range letters {
			if string(ch) != letter {
				fmt.Println(string(ch) + strconv.Itoa(number))
			}
		}
	}
}
