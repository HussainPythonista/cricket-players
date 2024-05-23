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
  
    delete_player_info(player_id:any):Observable<any>{
      return this.http.delete<any>(`${this.apiUrl}/delete_one_data/${player_id}`)
    }
  
    delete_all_data():Observable<any>{
      return this.http.delete<any>(`${this.apiUrl}/delete_all_data`)
    }

    single_player(player_no:any):Observable<any>{
      return this.http.get<any>(`${this.apiUrl}/one_student/${player_no}`)
    }
    delete_selected(player_no_list:any):Observable<any>{
      return this.http.delete<any>(`${this.apiUrl}/delete_selected/${player_no_list}`)
    }
}
