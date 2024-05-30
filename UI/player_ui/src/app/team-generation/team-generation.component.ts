import { CommonModule } from '@angular/common';
import { Component,OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { TeamService } from '../Services/team.service';
import { HttpClientModule } from '@angular/common/http';



@Component({
  selector: 'app-team-generation',
  standalone: true,
  imports: [CommonModule,FormsModule,HttpClientModule],
  templateUrl: './team-generation.component.html',
  styleUrl: './team-generation.component.css',
  providers:[TeamService]
})
export class TeamGenerationComponent implements OnInit {

  constructor(private teamService:TeamService){
  }
  number_of_teams:number=0
  teams:any;
  
  ngOnInit(): void {
    this.delete_team()
  }

  get_team(){
    this.teamService.get_team().subscribe(
      (response)=>{
        this.teams=response
      },(error)=>{
        console.log(error)
      })
    }

    error_show:string=''
    error:boolean=false
    generate_teams(){
      this.error = false;
      var team_genrate={'team':this.number_of_teams}

      this.teamService.generate_teams_back(team_genrate).subscribe(
        (response)=>{
          
          if (typeof response=='string'){
            
            this.error_show=response
            console.log(this.error_show)
            this.error=true
          }
          else{
            this.get_team()
          }
        },(error)=>{
          console.log(error)
        }
      )
    }
    delete_team(){
      this.teamService.delete_teams().subscribe(
        (response)=>{
          console.log(response)
        }
      )
    }
  }