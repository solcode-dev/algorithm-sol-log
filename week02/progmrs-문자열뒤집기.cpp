#include <string>
#include <vector>
#include <stack>

using namespace std;

string solution(string my_string, int s, int e)
{

  stack<int> st;
  // 1. 인덱스 s~e까지 문자열을 순서대로 스택에 넣는다.
  for (int i = s; i <= e; i++)
  {
    st.push(my_string[i]);
  }

  // 2. 스택에서 순서대로 pop하면서 인덱스 s~e에 넣는다.
  for (int i = s; i <= e; i++)
  {
    my_string[i] = st.top(); // 읽고
    st.pop();                // 제거
  }

  return my_string;
}