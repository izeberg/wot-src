package net.wg.gui.battle.bob
{
   import flash.display.MovieClip;
   import net.wg.infrastructure.base.meta.IBobBattleLoadingMeta;
   import net.wg.infrastructure.base.meta.impl.BobBattleLoadingMeta;
   
   public class BobBattleLoading extends BobBattleLoadingMeta implements IBobBattleLoadingMeta
   {
       
      
      public var bg:MovieClip = null;
      
      public function BobBattleLoading()
      {
         super();
      }
      
      override public function updateStage(param1:Number, param2:Number) : void
      {
         super.updateStage(param1,param2);
         this.bg.x = param1 >> 1;
         this.bg.y = param2 >> 1;
      }
      
      public function as_setBloggerIds(param1:Number, param2:Number) : void
      {
         BobBattleLoadingForm(form).setBloggerIds(param1,param2);
      }
   }
}
