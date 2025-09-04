package net.wg.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.gui.battle.components.BattleDisplayable;
   import net.wg.gui.battle.windows.vo.IngameDetailsKeyVO;
   import net.wg.infrastructure.exceptions.AbstractException;
   
   public class BattleHintPanelMeta extends BattleDisplayable
   {
       
      
      public var onPlaySound:Function;
      
      public var onHideComplete:Function;
      
      private var _ingameDetailsKeyVO:IngameDetailsKeyVO;
      
      public function BattleHintPanelMeta()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         if(this._ingameDetailsKeyVO)
         {
            this._ingameDetailsKeyVO.dispose();
            this._ingameDetailsKeyVO = null;
         }
         super.onDispose();
      }
      
      public function onPlaySoundS(param1:String) : void
      {
         App.utils.asserter.assertNotNull(this.onPlaySound,"onPlaySound" + Errors.CANT_NULL);
         this.onPlaySound(param1);
      }
      
      public function onHideCompleteS() : void
      {
         App.utils.asserter.assertNotNull(this.onHideComplete,"onHideComplete" + Errors.CANT_NULL);
         this.onHideComplete();
      }
      
      public final function as_setData(param1:Object, param2:String, param3:String, param4:int, param5:int, param6:Boolean, param7:Boolean) : void
      {
         var _loc8_:IngameDetailsKeyVO = this._ingameDetailsKeyVO;
         this._ingameDetailsKeyVO = new IngameDetailsKeyVO(param1);
         this.setData(this._ingameDetailsKeyVO,param2,param3,param4,param5,param6,param7);
         if(_loc8_)
         {
            _loc8_.dispose();
         }
      }
      
      protected function setData(param1:IngameDetailsKeyVO, param2:String, param3:String, param4:int, param5:int, param6:Boolean, param7:Boolean) : void
      {
         var _loc8_:String = "as_setData" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc8_);
         throw new AbstractException(_loc8_);
      }
   }
}
