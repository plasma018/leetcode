func removeOuterParentheses(S string) string {
    result := ""
	level := 0
	for _, x := range S {
		if x == 40 {
			if level > 0 {
				result += string(x)
			}
			level += 1
		} else {
			level -= 1
			if level > 0 {
				result += string(x)
			}
		}
	}
    return result
}
