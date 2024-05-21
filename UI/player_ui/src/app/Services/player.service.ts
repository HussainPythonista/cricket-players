import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Player } from '../../models/player.models';

@Injectable({
  providedIn: 'root'
})
export class PlayerService {
  private apiUrl = 'http://localhost:5000'; // Replace with your Flask API URL


  constructor(private http: HttpClient) { }


  getPlayers(): Observable<any> {

    const url =`${this.apiUrl}/players`
    return this.http.get<Player>(url)
    //return this.http.get(this.apiUrl);
  }
  add_players(players_info:Player):Observable<any>{
      //studentData.roll_no = studentData.roll_no;
      return this.http.post<Player>(`${this.apiUrl}/insert_one`, players_info);
    }
  
}
