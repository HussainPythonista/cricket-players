import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class TeamsService {
  private apiUrl = 'http://localhost:5000'; // Replace with your Flask API URL


  constructor(private http: HttpClient) { }
  
  getTeams():Observable<any>{
    const url =`${this.apiUrl}`
    return this.http.get<any>(url)
  }
}
