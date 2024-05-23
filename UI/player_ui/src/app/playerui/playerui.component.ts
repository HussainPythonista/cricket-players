import { CommonModule } from '@angular/common';
import { Component,OnInit  } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { FormControl } from '@angular/forms';
import { PlayerService } from '../Services/player.service';
import { HttpClientModule } from '@angular/common/http';
import { Player } from '../../models/player.models';


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
  display_check:boolean=false
  ascending:boolean=false
  player_list:Player[]=[]
  sort:boolean=false
  all_checked:boolean=false
  edit_player_bool:boolean=false

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
        console.log(this.get_all_players())
      
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
    sortedData:Player[]=[]
    needToSort(col_sort:any){
      this.sort=true
      this.ascending=!this.ascending
      if (col_sort=="name"){
        if  (this.ascending==false){
          this.sortedData= this.player_list.sort((a:any,b:any)=>a.name.localeCompare(b.name))
        }
        else{
          this.sortedData=this.player_list.sort((a:any,b:any)=>b.name.localeCompare(a.name))
        }
      }


      if (col_sort=="age"){
        if  (this.ascending==false){
          this.sortedData= this.player_list.sort((a:any,b:any)=>a.age-b.age)
        }
        else{
          this.sortedData=this.player_list.sort((a:any,b:any)=>b.age-a.age)
        }
      }

      if (col_sort=="batting_rating"){
        if  (this.ascending==false){
          this.sortedData= this.player_list.sort((a:any,b:any)=>a.batting_rating-b.batting_rating)
        }
        else{
          this.sortedData= this.player_list.sort((a:any,b:any)=>b.batting_rating-a.batting_rating)
        }
      }

      if (col_sort=="bowling_rating"){
        if  (this.ascending==false){
          this.sortedData=this.player_list.sort((a:any,b:any)=>a.bowling_rating-b.bowling_rating)
        }
        else{
          this.sortedData=this.player_list.sort((a:any,b:any)=>b.bowling_rating-a.bowling_rating)
        }
      }

      if (col_sort=="wicket_keeper_rating"){
        if  (this.ascending==false){
          this.sortedData=this.player_list.sort((a:any,b:any)=>a.wicket_keeper_rating-b.wicket_keeper_rating)
        }
        else{
          this.sortedData=this.player_list.sort((a:any,b:any)=>b.wicket_keeper_rating-a.wicket_keeper_rating)
        }
      }
    }

    checkAll(){
      this.all_checked=!this.all_checked
    }
    delete_selected_data(){
      if (this.all_checked){
        this.playerService.delete_all_data().subscribe(
          (response)=>
            
            this.display_check=true
            
        )
      }
    }
    delete_record(id:number){
      this.playerService.delete_player_info(id).subscribe(
        (response)=>{
          this.get_all_players()
        }
      )
    }

    find_one_player(id:any){
      
    }
    edit_player_info(id:any){
      console.log(id)

    }
}