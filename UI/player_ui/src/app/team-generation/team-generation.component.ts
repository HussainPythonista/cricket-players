import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { TeamService } from '../Services/team.service';
import { HttpClientModule } from '@angular/common/http';
import { response } from 'express';
import { error } from 'console';


@Component({
  selector: 'app-team-generation',
  standalone: true,
  imports: [CommonModule,FormsModule,HttpClientModule],
  templateUrl: './team-generation.component.html',
  styleUrl: './team-generation.component.css',
  providers:[TeamService]
})
export class TeamGenerationComponent {

  constructor(private teamService:TeamService){
  }
  number_of_teams:number=0
  teams:any;
  team_name:any;
  teamsData: any;
  teamsPerRow: number=0;
  generate_teams(){
    this.teamService.get_team().subscribe(
      (response)=>{
        this.teams=response
        
      },(error)=>{
        console.log(error)
      })
    }
    getRowIndices(): number[] {
      const rowCount = Math.ceil(this.teamsData.length / this.teamsPerRow);
      return Array.from({ length: rowCount }, (_, index) => index);
    }
    
    getTeamsForRow(rowIndex: number): any[] {
      const startIndex = rowIndex * this.teamsPerRow;
      const endIndex = Math.min(startIndex + this.teamsPerRow, this.teamsData.length);
      return this.teamsData.slice(startIndex, endIndex);
    }
  
  }