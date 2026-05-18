class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> map;
        map[')'] = '(';
        map[']'] = '[';
        map['}'] = '{';

        stack<char> stk;

        for (char &c : s) {
            if (map.find(c) == map.end()) {
                stk.push(c);
            } else {
                if (stk.empty()) {
                    return false;
                } else {
                    if (stk.top() == map[c]) {
                        stk.pop();
                    } else {
                        return false;
                    }
                }
            }
        }
        return stk.empty();
    }
};
