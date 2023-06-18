package main

import (
	"fmt"
	"strconv"
)

func LinearSearch[T comparable](arr []T, value T) int {
	for i := 0; i < len(arr); i++ {
		if arr[i] == value {
			return i
		}
	}
	return -1
}

func main() {
	slice := []string{"a", "b", "c", "z", "hello"}
	found_index := LinearSearch(slice, "z")
	fmt.Printf(strconv.Itoa(found_index))
}
