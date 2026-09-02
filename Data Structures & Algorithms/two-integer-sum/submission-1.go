func twoSum(nums []int, target int) []int {
    sums := make(map[int]int)

    for i,val := range nums {
        if j,ok := sums[val]; ok {
            return []int{j,i} 
        }
        sums[target-val] = i
    }

    return []int{}
}