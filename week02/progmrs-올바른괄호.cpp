#include <string>
using namespace std;

bool solution(string s)
{
  int cnt = 0;
  for (char c : s)
  {
    if (c == '(')
    {
      ++cnt;
    }
    else
    {                // ')'
      if (--cnt < 0) // 닫는 괄호가 더 많아지는 순간
        return false;
    }
  }
  return cnt == 0; // 열린 괄호가 남아있으면 false
}