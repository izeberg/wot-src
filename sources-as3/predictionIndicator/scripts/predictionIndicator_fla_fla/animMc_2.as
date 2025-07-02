package predictionIndicator_fla_fla
{
   import flash.display.MovieClip;
   
   public dynamic class animMc_2 extends MovieClip
   {
       
      
      public function animMc_2()
      {
         super();
         addFrameScript(0,this.frame1,20,this.frame21);
      }
      
      function frame1() : *
      {
         stop();
      }
      
      function frame21() : *
      {
         gotoAndPlay(2);
      }
   }
}
