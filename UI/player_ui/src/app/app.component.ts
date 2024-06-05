import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { CommonModule } from '@angular/common';
import { LoginService } from './Services/login.service';
import { TeamGenerationComponent } from './team-generation/team-generation.component';
import { FormtestComponent } from './formtest/formtest.component';
FormtestComponent



@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,LoginComponent,CommonModule,TeamGenerationComponent,FormtestComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
  //providers:[LoginService]
})
export class AppComponent {
  title = 'Mohamed ';
  count=0
  
  constructor (public loginService:LoginService){
    
    console.log("log from App",this.isLogged)
  }
  //   this.loginService.logIn
  //   console.log(this.loginService.isLoggedIn())
  // }
  
  isLogged=this.loginService.login

}
 
