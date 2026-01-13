package net.wg.frontline.infrastructure.base.meta.impl
{
   import net.wg.data.constants.Errors;
   import net.wg.frontline.gui.battle.views.data.PlayListsVO;
   import net.wg.gui.components.carousels.VehiclesFilterPopoverView;
   import net.wg.infrastructure.exceptions.AbstractException;
   
   public class FrontlineCarouselFilterPopoverMeta extends VehiclesFilterPopoverView
   {
       
      
      public var onPlayListsChange:Function;
      
      private var _playListsVO:PlayListsVO;
      
      public function FrontlineCarouselFilterPopoverMeta()
      {
         super();
      }
      
      override protected function onDispose() : void
      {
         if(this._playListsVO)
         {
            this._playListsVO.dispose();
            this._playListsVO = null;
         }
         super.onDispose();
      }
      
      public function onPlayListsChangeS(param1:String) : void
      {
         App.utils.asserter.assertNotNull(this.onPlayListsChange,"onPlayListsChange" + Errors.CANT_NULL);
         this.onPlayListsChange(param1);
      }
      
      public final function as_updatePlayLists(param1:Object) : void
      {
         var _loc2_:PlayListsVO = this._playListsVO;
         this._playListsVO = new PlayListsVO(param1);
         this.updatePlayLists(this._playListsVO);
         if(_loc2_)
         {
            _loc2_.dispose();
         }
      }
      
      protected function updatePlayLists(param1:PlayListsVO) : void
      {
         var _loc2_:String = "as_updatePlayLists" + Errors.ABSTRACT_INVOKE;
         DebugUtils.LOG_ERROR(_loc2_);
         throw new AbstractException(_loc2_);
      }
   }
}
