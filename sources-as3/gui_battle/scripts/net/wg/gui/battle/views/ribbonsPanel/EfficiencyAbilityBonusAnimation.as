package net.wg.gui.battle.views.ribbonsPanel
{
   import org.idmedia.as3commons.util.StringUtils;
   
   public class EfficiencyAbilityBonusAnimation extends EfficiencyBonusAnimation
   {
       
      
      public function EfficiencyAbilityBonusAnimation()
      {
         super();
      }
      
      override public function update(param1:String, param2:String) : void
      {
         visible = StringUtils.isNotEmpty(param2);
         if(visible)
         {
            image.visible = !_isExtendedAnim;
            image.imageName = param2;
            if(_isExtendedAnim)
            {
               imageFx.imageName = param2;
            }
         }
      }
   }
}
