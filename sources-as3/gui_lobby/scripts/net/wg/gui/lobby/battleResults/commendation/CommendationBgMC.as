package net.wg.gui.lobby.battleResults.commendation
{
   import flash.display.MovieClip;
   
   public class CommendationBgMC extends MovieClip
   {
       
      
      public function CommendationBgMC()
      {
         super();
      }
      
      public function switchDefault() : void
      {
         gotoAndStop(1);
      }
      
      public function switchState1() : void
      {
         gotoAndStop(2);
      }
      
      public function switchState2() : void
      {
         gotoAndStop(3);
      }
      
      public function switchState3() : void
      {
         gotoAndStop(4);
      }
   }
}
