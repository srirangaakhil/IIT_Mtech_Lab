#include<iostream>
#include<vector>
#include <map> 

using namespace std;

int main() {
	int n;
	int i;
	map<string, string> empBossMap;
	string emp, boss, s, b;

	cin >> n;	
	for(i = 0; i < n; i++) {
		cin >> emp >> boss;
		empBossMap.insert(pair<string, string>(emp, boss)); 
	}
	cin >> s >> b;

	i = 0;
	while(i <= n) {
		if(empBossMap[s] == b) {
			cout << "1" << endl;
			return 0;
		}
		s = empBossMap[s];
		i++;
	}
	cout << "0" << endl;
	return 0;
}