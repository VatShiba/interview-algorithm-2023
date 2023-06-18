package main

import (
	"fmt"
	"math"
	"strconv"
)

func BinarySearch(arr []int, value int) int {
	left_index := 0
	right_index := len(arr) - 1
	for left_index <= right_index {
		middle_index := int(math.Floor((float64(left_index) + float64(right_index)) / 2))
		if value == arr[middle_index] {
			return middle_index
		}
		if value < arr[middle_index] {
			right_index = middle_index - 1
		} else {
			left_index = middle_index + 1
		}
	}
	return -1
}

func main() {
	slice := []int{1, 2, 3, 4, 5, 6, 7, 50, 100}
	var found_index int = BinarySearch(slice, 7)
	fmt.Printf(strconv.Itoa(found_index))
}
