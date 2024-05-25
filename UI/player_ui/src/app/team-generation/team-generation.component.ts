import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-team-generation',
  standalone: true,
  imports: [CommonModule,FormsModule],
  templateUrl: './team-generation.component.html',
  styleUrl: './team-generation.component.css'
})
export class TeamGenerationComponent {

  number_of_teams:number=0
  generate_teams(){
    console.log(`${this.number_of_teams}  will generate`)
  }
}
