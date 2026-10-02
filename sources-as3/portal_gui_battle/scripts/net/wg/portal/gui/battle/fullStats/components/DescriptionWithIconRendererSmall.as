package net.wg.portal.gui.battle.fullStats.components
{
   public class DescriptionWithIconRendererSmall extends DescriptionWithIconRenderer
   {
      
      private static const SMALL_POSTFIX:String = "_small";
       
      
      public function DescriptionWithIconRendererSmall()
      {
         super();
         iconPostfix = SMALL_POSTFIX;
      }
   }
}
