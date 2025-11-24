#include <iostream>
#include <stack>
using namespace std;

int main()
{
  stack<char> left;
  stack<char> right;

  string s; // 입력받은 문자열
  cin >> s;

  // 초기 문자열을 left 스택에 넣기 (커서는 맨 뒤에 위치)
  for (int i = 0; i < s.length(); i++)
  {
    left.push(s[i]);
  }

  int n; // 명령어 갯수
  cin >> n;

  while (n--)
  {
    string cmd;
    cin >> cmd; // 명령
    if (cmd == "L")
    {
      if (!(left.empty()))
      {
        right.push(left.top());
        left.pop();
      }
    }
    else if (cmd == "D")
    {
      if (!(right.empty()))
      {
        left.push(right.top());
        right.pop();
      }
    }
    else if (cmd == "B")
    {
      if (!(left.empty()))
      {
        left.pop();
      }
    }
    else // cmd == P
    {
      char x;
      cin >> x;
      left.push(x);
    }
  }

  // left의 모든 문자를 right로 옮기기
  while (!left.empty())
  {
    right.push(left.top());
    left.pop();
  }

  // right에서 꺼내면서 출력 (역순이 원래 순서가 됨)
  while (!right.empty())
  {
    char x = right.top();
    cout << x;
    right.pop();
  }
}