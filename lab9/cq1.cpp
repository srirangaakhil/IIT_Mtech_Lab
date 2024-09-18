#include <iostream>
#include <map>
#include <string>
#include <queue>
#include <bits/stdc++.h> 
using namespace std;

typedef map<pair<string,string>, double> faretabletype;


void addfare(faretabletype &faretable, string origin, string destination, double fare) {
	pair <string, string> pair;
	pair.first = origin;
    pair.second = destination;
	faretable[pair] = fare;
}

bool getfare(faretabletype faretable, string origin, string destination, double &fare) {
	pair <string, string> pair;
	pair.first = origin;
    pair.second = destination;

    if(faretable.find(pair) == faretable.end()) 
  		return false;
	else {
		fare = faretable[pair];
  		return true;
	}
}

string connections(faretabletype faretable, string origin) {
	multimap<string, string> citymap;
	queue <string> q;
	map<string,int> status;
	string city;
	vector<string> connected_cities;
	string connected_cities_str = "";

	for (auto& x: faretable) 
    	citymap.insert(make_pair(x.first.first, x.first.second));

  	q.push(origin);
	status[origin] = 1;

	while(!q.empty()) {
		city = q.front();
		for (auto& x: citymap) {
    		if((city == x.first) && (status.find(x.second) == status.end())) {
    			q.push(x.second);
    			status[x.second] = 1;
    			connected_cities.push_back(x.second);
    		}
  		} 
  		q.pop();
  		status[city] = 2;
	}

	sort(connected_cities.begin(), connected_cities.end());

	connected_cities_str = "";
	for(int i = 0; i < connected_cities.size(); i++) {
		connected_cities_str =  connected_cities_str +  connected_cities[i];
		if(i != connected_cities.size() - 1)
			connected_cities_str =  connected_cities_str + " ";
	}
	return connected_cities_str;
}


int main() {
    faretabletype faretable; // create faretabletype using typedef

    while(true) {
        char command;
        cin >> command;
        if(command == 'x') break;
        if(command == 'a') {
            string origin, destination;
            cin >> origin >> destination;
            double fare;
            cin >> fare;
            addfare(faretable, origin, destination, fare);
        }
        else if(command == 'g') {
            string origin, destination;
            cin >> origin >> destination;
            double fare;
            bool found = getfare(faretable, origin, destination,fare);
            if(found) cout << fare <<endl;
            else cout << "Not found."<<endl;
        }
        else if(command == 'c') {
            string origin;
            cin >> origin;
            cout << connections(faretable, origin) << endl;
        }
        else cout <<"Illegal command."<<endl;
    }
    
}
