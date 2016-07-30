func twoSum(nums []int, target int) []int {
	rslt := []int{0, 0}
	for idx_1, v_1 := range nums {
		for idx_2, v_2 := range nums[idx_1+1:] {
			if v_1+v_2 == target {
				rslt[0] = idx_1
				rslt[1] = idx_2 + idx_1 + 1
				break
			}
		}
	}
	return rslt
}
