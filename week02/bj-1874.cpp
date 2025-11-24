#include <iostream>
#include <string>
#include <stack>
using namespace std;

int main()
{
  int n;
  stack<int> s;
  string ans;

  cin >> n;
  int m = 0; // 스택에 들어간 마지막 숫자

  while (n--)
  {
    int x;
    cin >> x;
    if (x > m) // 스택에 아직 x가 들어가지 않은 상태
    {
      while (x > m) // x까지 스택에 넣는다
      {
        s.push(++m);
        ans += '+';
      }
      s.pop(); // x가 스택의 맨 위에 오게 되었을 때 바로 꺼낸다. 이제 m == x.
      ans += '-';
    }
    else // 이미 스택 어딘가에 x가 들어가 있는 상태
    {
      bool found = false;
      if (!s.empty())
      {
        int top = s.top();
        s.pop();
        ans += '-';
        if (x == top)
        {
          found = true;
        }
      }
      if (!found) // 스택에서 지금 x를 꺼낼 수 없는 상태
      {
        cout << "NO" << "\n";
        return 0;
      }
    }
  }
  for (auto x : ans) // ans안에 있는 모든 요소들을 처음부터 끝까지 하나씩 꺼내서 x담아 반복한다
  {
    cout << x << "\n";
  }
  return 0;
}