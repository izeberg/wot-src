package net.wg.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.gui.battle.battleloading.BaseBattleLoading;
   import net.wg.gui.battle.mapsTraining.views.data.MapsTrainingBattleLoadingVO;
   import net.wg.gui.bootcamp.data.BCTutorialPageVO;
   import net.wg.infrastructure.exceptions.AbstractException;
   
   public class MapsTrainingBattleLoadingMeta extends BaseBattleLoading
   {
       
      
      public var gotoBattle:Function;
      
      private var _mapsTrainingBattleLoadingVO:MapsTrainingBattleLoadingVO;
      
      private var _vectorBCTutorialPageVO:Vector.<BCTutorialPageVO>;
      
      public function MapsTrainingBattleLoadingMeta()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         var _loc1_:BCTutorialPageVO = null;
         if(this._mapsTrainingBattleLoadingVO)
         {
            this._mapsTrainingBattleLoadingVO.dispose();
            this._mapsTrainingBattleLoadingVO = null;
         }
         if(this._vectorBCTutorialPageVO)
         {
            for each(_loc1_ in this._vectorBCTutorialPageVO)
            {
               _loc1_.dispose();
            }
            this._vectorBCTutorialPageVO.splice(0,this._vectorBCTutorialPageVO.length);
            this._vectorBCTutorialPageVO = null;
         }
         super.onDispose();
      }
      
      public function gotoBattleS() : void
      {
         App.utils.asserter.assertNotNull(this.gotoBattle,"gotoBattle" + Errors.CANT_NULL);
         this.gotoBattle();
      }
      
      public final function as_setData(param1:Object) : void
      {
         var _loc2_:MapsTrainingBattleLoadingVO = this._mapsTrainingBattleLoadingVO;
         this._mapsTrainingBattleLoadingVO = new MapsTrainingBattleLoadingVO(param1);
         this.setData(this._mapsTrainingBattleLoadingVO);
         if(_loc2_)
         {
            _loc2_.dispose();
         }
      }
      
      public final function as_setDataPage(param1:Array) : void
      {
         var _loc5_:BCTutorialPageVO = null;
         var _loc2_:Vector.<BCTutorialPageVO> = this._vectorBCTutorialPageVO;
         this._vectorBCTutorialPageVO = new Vector.<BCTutorialPageVO>(0);
         var _loc3_:uint = param1.length;
         var _loc4_:int = 0;
         while(_loc4_ < _loc3_)
         {
            this._vectorBCTutorialPageVO[_loc4_] = new BCTutorialPageVO(param1[_loc4_]);
            _loc4_++;
         }
         this.setDataPage(this._vectorBCTutorialPageVO);
         if(_loc2_)
         {
            for each(_loc5_ in _loc2_)
            {
               _loc5_.dispose();
            }
            _loc2_.splice(0,_loc2_.length);
         }
      }
      
      protected function setData(param1:MapsTrainingBattleLoadingVO) : void
      {
         var _loc2_:String = "as_setData" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
      
      protected function setDataPage(param1:Vector.<BCTutorialPageVO>) : void
      {
         var _loc2_:String = "as_setDataPage" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
   }
}
