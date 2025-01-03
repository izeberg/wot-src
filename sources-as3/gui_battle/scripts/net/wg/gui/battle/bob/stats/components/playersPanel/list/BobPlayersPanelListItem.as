package net.wg.gui.battle.bob.stats.components.playersPanel.list
{
   import flash.filters.DropShadowFilter;
   import flash.geom.ColorTransform;
   import net.wg.data.constants.InvalidationType;
   import net.wg.data.constants.generated.BATTLEATLAS;
   import net.wg.gui.battle.random.views.stats.components.playersPanel.constants.PlayersPanelInvalidationType;
   import net.wg.gui.battle.random.views.stats.components.playersPanel.list.PlayersPanelListItem;
   import net.wg.infrastructure.managers.IColorSchemeManager;
   
   public class BobPlayersPanelListItem extends PlayersPanelListItem
   {
      
      private static const INVALID_BLOGGER_INFO:uint = InvalidationType.SYSTEM_FLAGS_BORDER << 1;
      
      private static const BOB_PLAYERS_LIST_ITEM_SCHEME_PREFIX:String = "blogger_";
      
      private static const PLAYERS_LIST_ITEM_BLOGGER_NAME_SCHEME:String = "playersListBloggerName";
      
      private static const SHADOW_FILTER_SIZE:int = 12;
      
      private static const SHADOW_FILTER_STRENGTH:int = 1;
      
      private static const SHADOW_FILTER_ALPHA:int = 1;
       
      
      private var _bloggerId:int = -1;
      
      private var _isBlogger:Boolean = false;
      
      private var _colorSchemeMgr:IColorSchemeManager;
      
      public function BobPlayersPanelListItem()
      {
         this._colorSchemeMgr = App.colorSchemeMgr;
         super();
      }
      
      override protected function onDispose() : void
      {
         this._colorSchemeMgr = null;
         super.onDispose();
      }
      
      override protected function draw() : void
      {
         super.draw();
         if(isInvalid(INVALID_BLOGGER_INFO))
         {
            if(this._isBlogger)
            {
               selfBg.visible = true;
               selfBg.imageName = BATTLEATLAS.PLAYERS_PANEL_BLOGGER_BG;
               selfBg.transform.colorTransform = this._colorSchemeMgr.getTransform(this.bloggerColorScheme);
            }
            else
            {
               selfBg.imageName = BATTLEATLAS.PLAYERS_PANEL_SELF_BG;
               selfBg.transform.colorTransform = new ColorTransform();
            }
         }
         if(isInvalid(PlayersPanelInvalidationType.SELECTED))
         {
            if(this._isBlogger)
            {
               selfBg.visible = true;
            }
         }
         if(isInvalid(PlayersPanelInvalidationType.PLAYER_SCHEME))
         {
            this.applyLabelsColorScheme();
         }
      }
      
      public function setBloggerInfo(param1:int, param2:Boolean) : void
      {
         if(this._bloggerId == param1 && this._isBlogger == param2)
         {
            return;
         }
         this._bloggerId = param1;
         this._isBlogger = param2;
         invalidate(INVALID_BLOGGER_INFO);
         invalidate(PlayersPanelInvalidationType.PLAYER_SCHEME);
      }
      
      private function applyLabelsColorScheme() : void
      {
         var _loc1_:uint = 0;
         var _loc2_:uint = 0;
         var _loc3_:DropShadowFilter = null;
         if(this._isBlogger)
         {
            _loc1_ = this._colorSchemeMgr.getRGB(PLAYERS_LIST_ITEM_BLOGGER_NAME_SCHEME);
            _loc2_ = this._colorSchemeMgr.getRGB(this.bloggerColorScheme);
            _loc3_ = new DropShadowFilter(0,0,_loc2_,SHADOW_FILTER_ALPHA,SHADOW_FILTER_SIZE,SHADOW_FILTER_SIZE,SHADOW_FILTER_STRENGTH);
            playerNameCutTF.filters = [_loc3_];
            playerNameFullTF.filters = [_loc3_];
            playerNameCutTF.textColor = _loc1_;
            playerNameFullTF.textColor = _loc1_;
         }
         else
         {
            playerNameCutTF.filters = [];
            playerNameFullTF.filters = [];
         }
      }
      
      private function get bloggerColorScheme() : String
      {
         return BOB_PLAYERS_LIST_ITEM_SCHEME_PREFIX + this._bloggerId;
      }
   }
}
