import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class TeamService {
  constructor(private http: HttpClient) {}
  private apiUrl = 'http://localhost:5000';
  

  get_team():Observable<any>{
    return this.http.get<any>(`${this.apiUrl}/teams`)
  }

  generate_teams_back(number_teams:any):Observable<any>{
    return this.http.post<any>(`${this.apiUrl}/generate_post`,number_teams)
  }
}
