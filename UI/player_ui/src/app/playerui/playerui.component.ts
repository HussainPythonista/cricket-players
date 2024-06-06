import { CommonModule } from '@angular/common';
import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormsModule, ReactiveFormsModule,Validators,FormArray,FormControl  } from '@angular/forms';
import { PlayerService } from '../Services/player.service';
import { HttpClientModule } from '@angular/common/http';
import { Player } from '../../models/player.models';

@Component({
  selector: 'app-playerui',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, HttpClientModule, FormsModule],
  templateUrl: './playerui.component.html',
  styleUrls: ['./playerui.component.css'],
  providers: [PlayerService]
})
export class PlayeruiComponent implements OnInit {
  add_player_bool: boolean = false;
  myForm: FormGroup;
  editForm!: FormGroup;
  bulkEditForm: FormGroup;
  display_check: boolean = false;
  ascending: boolean = false;
  player_list: Player[] = [];
  sort: boolean = false;
  all_checked: boolean = false;
  edit_player_roll: any;
  open: boolean = false;
  edit_player_id: number = 0;
  sort_using: string = '';
  sortedData: Player[] = [];
  text_search=''
  next_number:number=0
  bulkForm!:FormGroup;

  constructor(private fb: FormBuilder, public playerService: PlayerService, private cdr: ChangeDetectorRef) {
    this.myForm = this.fb.group({
      player_no: [''],
      name: ['',[Validators.required,Validators.minLength(3)]],
      age: ['',[Validators.required, Validators.min(1), Validators.max(100) ]],
      batting_rating: ['',[Validators.required, Validators.min(1), Validators.max(10)]],
      bowling_rating: ['',[Validators.required, Validators.min(1), Validators.max(10)]],
      wicket_keeper_rating: ['',[Validators.required, Validators.min(1), Validators.max(10)]]
    });

    this.bulkEditForm = this.fb.group({
      players: this.fb.array([])
    });
    this.bulkForm=this.fb.group({
      batting_rating: ['',[Validators.required, Validators.min(1), Validators.max(10)]],
      bowling_rating: ['',[Validators.required, Validators.min(1), Validators.max(10)]],
      wicket_keeper_rating: ['',[Validators.required, Validators.min(1), Validators.max(10)]]
    })

    
  }


  add_player_check() {
    this.next_number=(this.player_list.reduce((max, player) => player.player_no > max ? player.player_no : max, 0)+1)
    if (this.edit_player_roll != null) {
      this.cancel_edit();
    } else {
      this.add_player_bool = !this.add_player_bool;
      this.resetForm();
      console.log(this.add_player_bool);
    }
  }

  get_all_players() {
    this.playerService.getPlayers().subscribe((response) => {
      this.player_list = response.sort((a: any, b: any) => b.player_no - a.player_no);
      this.applySort(); // Apply sorting after fetching data
      this.cdr.detectChanges();
      if (this.player_list.length==0){
        this.display_check=true
      }
      
      return this.player_list;
    });
  }


  ngOnInit() {
    this.get_all_players()
    this.get_selected_data(this.selected_data)
    console.log(this.player_list.length)
   
    
    
  }
  resetForm() {
    this.myForm.reset();
    this.editForm.reset();
  }

  onSubmit(): void {
    if (this.myForm.invalid) {
      // If the form is invalid, mark all fields as touched to trigger validation messages
      this.myForm.markAllAsTouched();
      return;
    }
    if (this.add_player_bool) {
      // Find the highest player number in the original player list
      const highestPlayerNo = this.player_list.reduce((max, player) => player.player_no > max ? player.player_no : max, 0);
      const newPlayerNo = highestPlayerNo + 1;
      this.myForm.value['player_no'] = newPlayerNo;
  
      this.playerService.add_players(this.myForm.value).subscribe((response) => {
        this.get_all_players();
        this.resetForm();
        console.log(response);
      });
    } else if (this.edit_player_roll != null) {
      this.myForm.value['player_no'] = this.edit_player_roll;
      this.playerService.add_players(this.myForm.value).subscribe((response) => {
        this.get_all_players();
        this.cancel_edit();
        console.log(response);
      });
    }
  }

  needToSort(col_sort: any) {
    this.sort_using = col_sort;
    this.sort = true;
    this.ascending = !this.ascending;
    this.applySort();
    this.cdr.detectChanges();
  }

  applySort() {


    
    if (this.sort_using === 'name') {
      this.sortedData = this.player_list.sort((a: any, b: any) =>
        this.ascending ? a.name.localeCompare(b.name) : b.name.localeCompare(a.name)
      );
    } else if (this.sort_using === 'age') {
      this.sortedData = this.player_list.sort((a: any, b: any) =>
        this.ascending ? a.age - b.age : b.age - a.age
      );
    } else if (this.sort_using === 'batting_rating') {
      this.sortedData = this.player_list.sort((a: any, b: any) =>
        this.ascending ? a.batting_rating - b.batting_rating : b.batting_rating - a.batting_rating
      );
    } else if (this.sort_using === 'bowling_rating') {
      this.sortedData = this.player_list.sort((a: any, b: any) =>
        this.ascending ? a.bowling_rating - b.bowling_rating : b.bowling_rating - a.bowling_rating
      );
    } else if (this.sort_using === 'wicket_keeper_rating') {
      this.sortedData = this.player_list.sort((a: any, b: any) =>
        this.ascending ? a.wicket_keeper_rating - b.wicket_keeper_rating : b.wicket_keeper_rating - a.wicket_keeper_rating
      );
    } else if (this.sort_using==='player_no') {
      this.sortedData = this.player_list.sort((a: any, b: any) =>
        this.ascending ? a.player_no - b.player_no : b.player_no - a.player_no
      );
    }
  }

  checkAll() {
    this.all_checked = !this.all_checked;
  }

  selected_data: any[] = [];
  
  delete_all: boolean = false;
  delete_selected(selected_data: any) {
    if (this.all_checked) {
      this.playerService.delete_all_data().subscribe((response) => {
        this.display_check = true;
        this.get_all_players();
      });
    } else {
      this.playerService.delete_selected(selected_data).subscribe((response) => {
        console.log(response);
        this.get_all_players();
      });
    }
  }

  delete_sort: boolean = false;
  delete_record(id: number) {
    this.playerService.delete_player_info(id).subscribe((response) => {
      this.get_all_players();
      if (this.sort) {
        this.applySort();
      }
      this.cdr.detectChanges();
    });
  }

  single_player_info: any;
  find_one_player(id: any) {
    this.playerService.single_player(id).subscribe((response) => {
      this.single_player_info = response;
      console.log(response);
    });
  }

  cancel_edit() {
    this.edit_player_roll = null;
  }

  single_data: any;
  edit_player_info(id: any) {
    this.edit_player_roll = id;
    if (this.add_player_bool) this.add_player_check();
    this.playerService.single_player(id).subscribe((response) => {
      this.single_data = response;
      
    });
  }

  save_edit: boolean = false;
  save_edit_data() {
    this.save_edit = !this.save_edit;
  }

  updated_player_info() {
    console.log(this.editForm.value);
  }

  
  
  search:boolean=false
  handleKeyDown(pressedKey:any){
    this.search=true
    if (pressedKey.keyCode==8){
      //console.log(pressedKey.keyCode)
      this.text_search=this.text_search.slice(0,-1)
      console.log(this.text_search)
      this.getPlayerSearch(this.text_search)
      
    }
    else if (pressedKey.keyCode >= 65 && pressedKey.keyCode <= 90){
      
        this.text_search+=pressedKey.key
        this.getPlayerSearch(this.text_search)
    }
    if (this.text_search.length==0){
        this.search=false
      }
      console.log(this.search)
  }

  
  selected_players(player_no: any) {
    var present=this.selected_data.includes(player_no)
    if (this.all_checked==false){
      if (present){
        const index = this.selected_data.indexOf(player_no);
        this.selected_data.splice(index,1)
        console.log(this.selected_data)
 
      }
      
      else{
        this.selected_data.push(player_no);
        console.log(this.selected_data)
      }
    } 
    
   }

   filered_data:any=[]
   getPlayerSearch(text:any){
     console.log(text)
     var filterData=this.player_list.filter((item) =>
       item.name.toLowerCase().includes(text.toLowerCase())
     )
     this.filered_data=filterData
     
   }


 data_bulk_update:any;
 get_selected_data(playerList:any){
      if (playerList.length!=0){
        this.playerService.get_list_players(playerList).subscribe(
          (response)=>{
            this.data_bulk_update= response
            this.bulk_edit=true
            this.initializeForm(this.data_bulk_update);
            
          }
        )}
      }

  bulk_edit:boolean=false
  
  cancel_bulk_update(){
    this.bulk_edit=false
    this.selected_data=[]
    this.bulk_update_con=false
    this.all_checked=false
    this.get_all_players()
  }
  edit_bulk(){
    this.get_selected_data(this.selected_data)
    
  }
  

  initializeForm(dataSet: any[]) {
    if (!dataSet) {
      return; // Exit early if dataSet is undefined or null
    }
  
    const playersArray = this.bulkEditForm.get('players') as FormArray;
    playersArray.clear(); // Clear existing form array before adding new data
  
    dataSet.forEach(player => {
      playersArray.push(this.createPlayerFormGroup(player));
    });
  }
  createPlayerFormGroup(player: any): FormGroup {
    return this.fb.group({
      player_no:[player.player_no],
      name: [player.name],
      age: [player.age],
      batting_rating: [player.batting_rating,[Validators.required, Validators.min(1), Validators.max(10)]],
      bowling_rating: [player.bowling_rating,[Validators.required, Validators.min(1), Validators.max(10)]],
      wicket_keeper_rating: [player.wicket_keeper_rating,[Validators.required, Validators.min(1), Validators.max(10)]]
    });
  }
  get players(): FormArray {
    return this.bulkEditForm.get('players') as FormArray;
  }

  update_bulk_data() {
    console.log(this.bulkEditForm.value.players);
   
    this.cancel_bulk_update(); 
  }

  onSubmit_edit(){
    var data_to_post=this.bulkEditForm.value.players
    console.log(data_to_post)
    this.playerService.update_selected_players(data_to_post).subscribe(
      (response)=>{
        this.get_all_players()
        this.cancel_bulk_update()
        console.log(response)
      }
    )
  }
 // bulk_edit:boolean=false
  bulk_update_con:boolean=false
  bulk_update(){
    this.bulk_update_con=true

    //Update all the values in single selection
    if (this.all_checked==true){
      this.selected_data=[]
      for (let i = 0; i < this.player_list.length; i++){
        this.selected_data.push(this.player_list[i]['player_no'])
      }
      
    }
    //console.log(this.selected_data)

    
  }
  onSubmit_bulk(){
    var data=this.bulkForm.value
    this.playerService.bulk_update(data,this.selected_data).subscribe(
      (response)=>{
        console.log(response)
        this.get_all_players()
        this.cancel_bulk_update()
        this.bulkForm.reset()
      }
    )
    
  }
}
