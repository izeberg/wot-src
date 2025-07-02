package
{
   import net.wg.gui.components.damageIndicator.AnimationContainer;
   
   public dynamic class ExtendedAnimationUI extends AnimationContainer
   {
       
      
      public function ExtendedAnimationUI()
      {
         addFrameScript(11,this.frame12);
         super();
      }
      
      function frame12() : *
      {
         stop();
      }
   }
}
