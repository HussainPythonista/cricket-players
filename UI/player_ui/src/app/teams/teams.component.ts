import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { TeamsService } from '../Services/teams.service';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-teams',
  standalone: true,
  imports: [CommonModule,FormsModule,HttpClientModule],
  templateUrl: './teams.component.html',
  styleUrl: './teams.component.css'
})
export class TeamsComponent {
  numDivs: number=0
  rows: number[][] = [];

  constructor(){}


  get_all_teams(){
    
  }
}
