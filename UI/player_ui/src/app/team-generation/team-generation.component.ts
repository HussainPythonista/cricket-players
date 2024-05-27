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
    this.get_team()
  }

  get_team(){
    this.teamService.get_team().subscribe(
      (response)=>{
        this.teams=response
      },(error)=>{
        console.log(error)
      })
    }

    generate_teams(){
      var team_genrate={'team':this.number_of_teams}
      this.teamService.generate_teams_back(team_genrate).subscribe(
        (response)=>{
          this.get_team()
          console.log(response)
        },(error)=>{
          console.log(error)
        }
      )
    }
  }