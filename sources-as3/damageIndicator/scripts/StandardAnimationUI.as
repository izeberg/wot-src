package
{
   import net.wg.gui.components.damageIndicator.AnimationContainer;
   
   public dynamic class StandardAnimationUI extends AnimationContainer
   {
       
      
      public function StandardAnimationUI()
      {
         addFrameScript(89,this.frame90);
         super();
      }
      
      function frame90() : *
      {
         stop();
      }
   }
}
