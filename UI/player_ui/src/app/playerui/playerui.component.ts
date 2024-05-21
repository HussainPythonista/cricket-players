import { CommonModule } from '@angular/common';
import { Component,OnInit,Input,ChangeDetectorRef  } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { FormControl } from '@angular/forms';
import { PlayerService } from '../Services/player.service';
import { HttpClientModule } from '@angular/common/http';
import { Player } from '../../models/player.models';
import { response } from 'express';

@Component({
  selector: 'app-playerui',
  standalone: true,
  imports: [CommonModule,ReactiveFormsModule,HttpClientModule],
  templateUrl: './playerui.component.html',
  styleUrl: './playerui.component.css',
  providers:[PlayerService]
})
export class PlayeruiComponent implements OnInit{
  add_player_bool:boolean=false;
  myForm: FormGroup;


  player_list:Player[]=[]
  add_player_check(){
        
        this.add_player_bool=!this.add_player_bool
        console.log(this.add_player_bool)
    }
    constructor(private fb: FormBuilder,public playerService:PlayerService) {
      this.myForm = this.fb.group({
        name: [''],
        age: [''],
        batting_rating: [''],
        bowling_rating:[''],
        wicket_keeper_rating:['']
      });
    }
    

    get_all_players(){
      this.playerService.getPlayers().subscribe(
        (response)=>{
          this.player_list=response
        }
      )
    }
    ngOnInit() {
      this.get_all_players()
    }
    onSubmit(): void {
      //this.player_list.unshift(this.myForm.value);
      this.playerService.add_players(this.myForm.value).subscribe(
        (response)=>{
          this.get_all_players()
          console.log(response)
        }
      )
    }
    
    delete_record(id:number){
      console.log(id,"will be delete")
    }
}