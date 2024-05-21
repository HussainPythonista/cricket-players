import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LoginService {
  login:boolean=false
  
  logedin(){
    this.login=true
  }
  
  logFailed(){
    this.login=false
  }
}
